from langchain.agents import AgentExecutor, create_structured_chat_agent
from langchain.tools import Tool
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
from typing import List, Dict, Any
import os

class TelecomAgent:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.llm = None
        self.agent_executor = None
        self.setup_llm()
        self.setup_agent()

    def setup_llm(self):
        """Initialize the Qwen 2.5 7B model"""
        try:
            model_name = "Qwen/Qwen1.5-7B"  # Update this to the correct model name/path
            self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name,
                device_map="auto",
                trust_remote_code=True
            )
            
            # Create a text generation pipeline
            pipe = pipeline(
                "text-generation",
                model=self.model,
                tokenizer=self.tokenizer,
                max_new_tokens=512,
                temperature=0.7,
                device_map="auto"
            )
            
            self.llm = HuggingFacePipeline(pipeline=pipe)
        except Exception as e:
            print(f"Error setting up LLM: {str(e)}")
            raise

    def setup_agent(self):
        """Setup the LangChain agent with tools"""
        tools = [
            Tool(
                name="analyze_cdr",
                func=self._analyze_cdr,
                description="Analyze Call Detail Records (CDR) data"
            ),
            Tool(
                name="analyze_revenue",
                func=self._analyze_revenue,
                description="Analyze revenue data and generate insights"
            ),
            Tool(
                name="process_file",
                func=self._process_file,
                description="Process and extract information from telecom files"
            )
        ]

        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an AI assistant specialized in analyzing telecom data. "
                      "Use the available tools to process queries and provide accurate insights."),
            ("human", "{input}"),
            ("assistant", "I'll help analyze that. Let me think step by step:\n{agent_scratchpad}")
        ])

        agent = create_structured_chat_agent(self.llm, tools, prompt)
        self.agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    def _analyze_cdr(self, query: str) -> str:
        """Analyze CDR data"""
        # TODO: Implement CDR analysis logic
        return "CDR analysis not implemented yet"

    def _analyze_revenue(self, query: str) -> str:
        """Analyze revenue data"""
        # TODO: Implement revenue analysis logic
        return "Revenue analysis not implemented yet"

    def _process_file(self, file_path: str) -> str:
        """Process telecom files"""
        # TODO: Implement file processing logic
        return f"Processing file: {file_path}"

    async def process_query(self, query: str) -> Dict[str, Any]:
        """Process a user query using the agent"""
        try:
            response = await self.agent_executor.arun(query)
            return {"response": response, "status": "success"}
        except Exception as e:
            return {"response": str(e), "status": "error"}

# Create a singleton instance
telecom_agent = TelecomAgent() 