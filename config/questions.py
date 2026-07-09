

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "resume/Rajkumar_Resume.pdf"      # Place your resume at project root under resume/ or update path

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience? 
years_of_experience = "1"          # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "No"               # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = "https://github.com/RajkumarDake"                        # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/rajkumar-dake-102670244/"       # "https://www.linkedin.com/in/example" or "" and so on...

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Non-citizen allowed to work for any employer"



## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 3000000          # ₹30 LPA = 3000000. Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
'''

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = 1450000            # ₹14.5 LPA. Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# What is your notice period in days?
notice_period = 60                   # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "Senior Software Engineer @ InfoEdge India | Multi-Agent AI Systems, LangGraph, MCP & FastAPI | B.Tech CSE, NIT Jamshedpur" # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
Senior Software Engineer at InfoEdge India (Noida), building a production Multi-Agent AI Platform using Google A2A, MCP, FastAPI, and React with dynamic agent discovery, orchestration, and parallel execution.
Previously built an MCP Server exposing 15+ AI tools, an LLM-powered feedback classification system, and secure REST APIs with RBAC and audit logging.
B.Tech in Computer Science from NIT Jamshedpur (CGPA 8.02). Skilled in Python, LangChain/LangGraph, RAG, FastAPI, PostgreSQL/pgvector, Docker, and distributed systems.
Codeforces Specialist (1448), CodeChef 4★ (1626), AIR 2/21,367 in CodeChef Starters 117.
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
I am Rajkumar Dake, a Senior Software Engineer at InfoEdge India with a B.Tech in CSE from NIT Jamshedpur. I have hands-on experience architecting multi-agent AI platforms with Google A2A, MCP, FastAPI, and LangGraph, along with RAG pipelines and distributed observability using Langfuse. I am eager to contribute to your team and grow with impactful projects. Open to opportunities in Bangalore, Hyderabad, and across India. Notice period: 60 days. Expected CTC: ₹30+ LPA.
"""

# Your user_information_all letter in quotes, use \n to add line breaks if using single quotes "user_information_all".You can skip \n if using triple quotes """user_information_all""" (This question makes sense though)
# Passed to AI to generate answers from - include resume-level info like name, experience, skills, etc.
user_information_all ="""
Name: Rajkumar Dake. Email: rajkumardakey831@gmail.com. Mobile: +91 7569009619. Location: Gopalapuram, Andhra Pradesh, India. Pincode: 534316. Gender: Male. Disability: No. Veteran: No. Work authorization: Eligible to work in India; no visa sponsorship required.

Education: B.Tech CSE, NIT Jamshedpur (Aug 2021–Jun 2025), CGPA 8.02/10.

Experience: Senior Software Engineer at InfoEdge India Ltd, Noida (Jun 2026–Present): architected a production Multi-Agent AI Platform using Google A2A, MCP, FastAPI, and React with dynamic agent discovery, orchestration, and parallel execution; built LLM-powered routing and query-understanding for intent detection and conversation memory resolution; built distributed observability/tracing with Langfuse; built a real-time AI conversational platform with SSE streaming and dynamic UI generation.
Software Engineer at InfoEdge India Ltd, Noida (Jul 2025–Jun 2026): built and deployed a production MCP Server exposing 15+ AI tools for search, comparison, sales workflows, and ticket classification; built an LLM-powered feedback categorization system reducing processing time from 2 minutes to 2 seconds; built a multi-agent orchestration platform for intent-based request routing; developed secure REST APIs with RBAC, audit logging, and analytics dashboards.

Skills: Python, C++, JavaScript; LangChain, LangGraph, Multi-Agent Systems, MCP, RAG; FastAPI, Async SQLAlchemy, Microservices, Distributed Systems; PostgreSQL, pgvector, MySQL, MongoDB; Langfuse, Docker, Linux, Git, GitHub, GitLab; Vite, HTML, CSS, JavaScript (frontend).

Projects: Multi-Agent AI Research Assistant (LangGraph agents for planning/retrieval/reasoning; RAG pipeline over PostgreSQL/pgvector across 10,000+ documents). LLM Gateway and Tool Execution Platform (centralized LLM Gateway with model routing, conversation memory, structured outputs, tool calling; scalable tool execution framework integrating APIs, databases, external services).

Achievements: Codeforces Specialist (Peak Rating 1448), CodeChef 4★ (Max Rating 1626), AIR 2/21,367 (Top 0.01%) in CodeChef Starters 117, AIR 52/23,120 in Starters 118, AIR 75 in a national-level coding contest by IIT Mandi. Notice period: 60 days. Current CTC: ₹14.5 LPA. Expected CTC: ₹30+ LPA. Preferred locations: Bangalore, Hyderabad, India. LinkedIn: linkedin.com/in/rajkumar-dake-102670244. GitHub: github.com/RajkumarDake.
"""
'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
'''

# Name of your most recent employer
recent_employer = "InfoEdge India Ltd" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "8"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = True         # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive




