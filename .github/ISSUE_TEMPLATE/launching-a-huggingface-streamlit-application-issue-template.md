---
name: Launching a HuggingFace Streamlit Application Issue Template
about: Steps to successfully build a Streamlit app from source code
title: ''
labels: enhancement
assignees: ''

---

# **Objective 1**: 
Use the files from the `/HuggingFace_Spaces` folder and create a HuggingFace Space using Docker Space sdk with the Streamlit Docker template

## **Step 1**:
 - Log into [Huggingface](https://huggingface.co/) and create a new Space

## **Step 2**:
 - Create a fitting Space Name
 - Use the following Short Description:
   > [FILL IN CONTENT HERE]

 - For License: Use the MIT License

   >Very permissive and widely used
   > Allows others to use, modify, and distribute your code with minimal restrictions
   > Good for open-source demos and educational projects

 - Use Docker for the Space sdk option and select to use the Streamlit Docker template for the application
 - Create a **Public** Space

## **Step 3**:
 - Upload the `/HuggingFace_Spaces/app` folder
 - Replace the existing `Dockerfile`, `requirements.txt`, and `README.md` files

## **Step 4**:
 - Monitor the Build
 
> It may complain about not finding the application files.
> If so:
> 1. Add [ADD MAIN SCRIPT HERE (ex. `app_file: app/main.py`] to the README.md file's header
> 2. Check the RUN command of the Dockerfile

## **Step 5**:
 - Interact with the application and briefly check for any issues
