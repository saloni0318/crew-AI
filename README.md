# CrewAI Vlog2Blog

An AI-driven workflow that converts YouTube channel content into structured blog posts using CrewAI, language models, and a YouTube search utility.

---

##  Overview

This project automates the process of turning video content into readable blog articles. It uses multiple AI agents working together—one for gathering information and another for writing polished content.

---

##  Functionality

- Builds a workflow using `crew.py` with two agents:
  - **Research Agent** – collects relevant data from YouTube videos  
  - **Writer Agent** – transforms collected insights into blog content  
- Initializes tools and environment settings through `tools.py`  
- Outputs the generated article into a Markdown file  

---

##  Important Files

- `crew.py` – Entry point that runs the workflow  
- `agents.py` – Defines AI agents and model configuration  
- `tasks.py` – Contains task logic for research and writing  
- `tools.py` – Handles environment setup and YouTube search tool  
- `requirements.txt` – Lists all required Python packages  
- `new-blog-post.md` – Stores generated blog output  

---

##  Requirements

- Python 3.11 or any compatible 3.x version  
- Virtual environment (recommended for isolation)  
- API access (either one):
  - OpenAI API key  
  - OpenRouter API key  

---

##  Setup Instructions

### 1. Create a virtual environment
python -m venv .venv

### 2. Activate the environment


### 3. Install dependencies
pip install -r requirements.txt

### 4. Configure environment variables

Create a `.env` file in the root directory and add:

OPENAI_API_KEY=your_api_key_here

or

OPENROUTER_API_KEY=your_api_key_here

---

##  Running the Project

1. Open `crew.py`  
2. Set the following inputs:
   - `topic` – topic you want to generate a blog on  
   - `youtube_channel_handle` – target YouTube channel  

3. Execute the script:
python crew.py

---

##  Output

- Blog content is:
  - Displayed in the terminal  
  - Saved to `new-blog-post.md`  

---

##  Customization

- Update topic/channel directly in `crew.py`  
- Modify task logic in `tasks.py`  
- Adjust agent behavior or model in `agents.py`  
- Extend or tweak tools via `tools.py`  

---

##  Model Details

Default model:
openrouter/minimax/minimax-m2.5:free

---

## Additional Notes

- Environment variables are auto-loaded from `.env`  
- OpenRouter configuration is handled internally when used  
- Lightweight design makes it easy to extend or integrate  


