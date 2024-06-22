from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import CSVLoader
from langchain_community.document_loaders import Docx2txtLoader
import tqdm

def load_files_from_directory(directory_path:str='./data', source_column:str=None) -> list:
    """
    Description: 
    Reads .txt, .pdf, .csv and .docx files in a directory/folder and turns them into a list of langchain 'Documents' objects, which contains page_content, metadata(source), page/row. 

    Args:
    directory_path: The path to the folder containing the files. 
    source_column: Name of the column in the CSV files that will be quoted as the source. Defaults to file location if set to none. 

    Returns:
    A list with langchain 'Document' objects
    """

    documents = []
    try: 
        txt_loader = DirectoryLoader(
            directory_path, glob="**/*.txt", loader_cls=TextLoader, show_progress=True
        )
        documents.extend(txt_loader.load())

        pdf_loader = DirectoryLoader(
            directory_path, glob="**/*.pdf", loader_cls=PyPDFLoader, show_progress=True
        )
        documents.extend(pdf_loader.load())

        csv_loader = DirectoryLoader(
            directory_path, glob="**/*.csv", loader_cls=CSVLoader, show_progress=True,
            loader_kwargs={"encoding":"utf8", "source_column":source_column}
        )
        documents.extend(csv_loader.load())

        doc_loader = DirectoryLoader(
            directory_path, glob="**/*.docx", loader_cls=Docx2txtLoader, show_progress=True,
        )
        
        documents.extend(doc_loader.load())
        return documents
    
    except Exception as e:
        print("Error loading files from directory:", e)

from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_files(documents:list, chunk_size:int=1000, chunk_overlap:int=50)->list:
    """
    Description: 
    Splits loaded Document into chunks of text. 
    You can experiment with chunk_size and chunk_overlap size for your specific case. 

    Args:
    documents: The loaded documents to split
    chunk_size: The size of the chunks. Defaults to 500. 
    chunk_overlap: siz of chunk_overlap. Defaults to 50. 

    Returns:
    A list of text chunks.
    """
    try:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap, separators = ["\n\n", "\n", " ", ""])
        chunks = text_splitter.split_documents(documents)
        print('Chunks created: ', len(chunks))
        return chunks
    except Exception as e:
        print("Error splitting files: ", e)


from typing import Type, Union
from dotenv import load_dotenv
load_dotenv()
from langchain_community.embeddings import OpenAIEmbeddings
import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def embeddings_and_create_faiss_vectorstore (chunks:list, embedding_model:Type[Union[HuggingFaceEmbeddings, OpenAIEmbeddings]]=HuggingFaceEmbeddings, specific_model:str='sentence-transformers/all-MiniLM-L6-v2') -> FAISS: 
    """  
    Description:
    Embeds the text chunks and saves it in a vectorstore. 

    Remember to have a .env file in the working directory with API keys for HuggingFace and OpenAI.

    Args: 
        chunks: A list of chunks from a Langchain loader. 
        embedding_model: Must be HuggingFaceEmbeddings or OpenAIEmbeddings. Defaults to HuggingFaceEmbeddings.
        specific_model: For example 'sentence-transformers/all-MiniLM-L6-v2' or 'gpt-3.5-turbo'. Defaults to'sentence-transformers/all-MiniLM-L6-v2'.

    Returns:
        None. It saves a FAISS vectorstore in a folder called 'vectorstore' in the current working directory.
    """
    # Validate that the embedding_model is either HuggingFaceEmbeddings or OpenAIEmbeddings
    if not issubclass(embedding_model, (HuggingFaceEmbeddings, OpenAIEmbeddings)):
        raise ValueError("embedding_model must be either HuggingFaceEmbeddings or OpenAIEmbeddings")
    
    try:
        embeddings = embedding_model(model_name=specific_model, show_progress=True)
        print("Embeddings created")
    except Exception as e:
        print("Error creating embeddings:", e)
        return  # Stop execution if embeddings cannot be created

    try:
        os.makedirs('./vectorstore', exist_ok=True)
        
        vectorstore = FAISS.from_documents(chunks, embeddings)
        vectorstore.save_local('./vectorstore/')
        print("Vectorstore created")
    except Exception as e:
        print("Error creating vectorstore:", e)


# ----------------------------------- Main function ---------------------------------- #

def directory_into_faiss_pipeline(directory_path:str, chunk_size:int, chunk_overlap:int, embedding_model:Type, specific_model:str) -> None:
    """
    Full pipeline to load data from a database, save it as CSV, create chunks, and embed into a FAISS vectorstore.

    Args:
        directory_path (str): Path to directory/folder 
        chunk_size (int): Size of the chunks.
        chunk_overlap (int): Size of the chunk overlap.
        embedding_model (Type): The class of the embedding model to use.
        specific_model (str): Specific model name for the embeddings.

    Returns:
        None. It saves a FAISS vectorstore in a folder called 'vectorstore' in the current working directory.
    """
    print("Starting data loading...", directory_path)
    documents = load_files_from_directory(directory_path)
    if not documents:
        print("No documents loaded, stopping process.")
        return

    print("Splitting documents...")
    chunks = split_files(documents, chunk_size, chunk_overlap)
    if not chunks:
        print("No chunks created, stopping process.")
        return

    print("Embedding chunks and creating vector store...")
    embeddings_and_create_faiss_vectorstore(chunks, embedding_model, specific_model)
    print("Vectorstore created successfully.")

# Example usage:
directory_into_faiss_pipeline(
    directory_path='./data', 
    chunk_size=1000,
    chunk_overlap=50, 
    embedding_model=HuggingFaceEmbeddings, 
    specific_model='sentence-transformers/all-MiniLM-L6-v2'
)