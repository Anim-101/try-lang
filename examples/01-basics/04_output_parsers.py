"""
04_output_parsers.py
Structuring LLM Outputs - Convert text responses to structured data
"""

import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from pydantic import BaseModel, Field
from typing import List

# Load environment variables
load_dotenv()

# Define data models for structured output
class Recipe(BaseModel):
    """Recipe data model"""
    name: str = Field(description="Name of the recipe")
    ingredients: List[str] = Field(description="List of ingredients")
    instructions: List[str] = Field(description="Step by step instructions")
    prep_time: int = Field(description="Preparation time in minutes")
    difficulty: str = Field(description="Difficulty level: Easy, Medium, or Hard")

class ProductReview(BaseModel):
    """Product review analysis model"""
    sentiment: str = Field(description="Overall sentiment: Positive, Negative, or Neutral")
    rating: int = Field(description="Estimated rating from 1-5 stars")
    key_points: List[str] = Field(description="Main points mentioned in the review")
    recommendation: str = Field(description="Would recommend: Yes, No, or Maybe")

def json_output_parser_example():
    """
    Use JsonOutputParser to get structured JSON output
    """
    print("📊 JSON Output Parser Example")
    print("=" * 35)
    
    # Create parser for Recipe model
    parser = JsonOutputParser(pydantic_object=Recipe)
    
    # Create prompt with format instructions
    prompt = PromptTemplate(
        template="""Create a simple recipe for {dish}.
        
{format_instructions}
        
Make sure to include realistic prep time and difficulty level.""",
        input_variables=["dish"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
    
    llm = OpenAI(temperature=0.3)
    
    # Create the chain
    chain = prompt | llm | parser
    
    return chain

def review_analysis_parser():
    """
    Parse and analyze product reviews
    """
    print("\n🔍 Review Analysis Parser Example")
    print("=" * 40)
    
    parser = JsonOutputParser(pydantic_object=ProductReview)
    
    prompt = PromptTemplate(
        template="""Analyze the following product review and extract structured information:

Review: "{review_text}"

{format_instructions}

Be accurate and objective in your analysis.""",
        input_variables=["review_text"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
    
    llm = OpenAI(temperature=0.2)
    chain = prompt | llm | parser
    
    return chain

def string_manipulation_parser():
    """
    Simple string output with custom processing
    """
    print("\n✂️ String Manipulation Example")
    print("=" * 35)
    
    # Custom output parser that cleans and formats the output
    class CleanOutputParser(StrOutputParser):
        def parse(self, text: str) -> str:
            # Remove extra whitespace and format nicely
            cleaned = text.strip()
            # Capitalize first letter of each sentence
            sentences = cleaned.split('. ')
            capitalized = [s.capitalize() for s in sentences if s]
            return '. '.join(capitalized)
    
    prompt = PromptTemplate.from_template(
        "write a short motivational quote about {topic}"
    )
    
    llm = OpenAI(temperature=0.8)
    custom_parser = CleanOutputParser()
    
    chain = prompt | llm | custom_parser
    
    return chain

def main():
    """
    Demonstrate different output parsers
    """
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Please set your OPENAI_API_KEY in .env file")
        return
    
    try:
        # 1. JSON Output Parser - Recipe
        recipe_chain = json_output_parser_example()
        
        print("Generating recipe for pasta...")
        recipe_result = recipe_chain.invoke({"dish": "spaghetti carbonara"})
        
        print(f"📋 Recipe Name: {recipe_result['name']}")
        print(f"⏰ Prep Time: {recipe_result['prep_time']} minutes")
        print(f"📈 Difficulty: {recipe_result['difficulty']}")
        print(f"🥘 Ingredients: {', '.join(recipe_result['ingredients'][:3])}...")
        
        # 2. Review Analysis Parser
        review_chain = review_analysis_parser()
        
        sample_reviews = [
            "This laptop is amazing! Super fast, great battery life, and the display is gorgeous. Highly recommend!",
            "Terrible product. Broke after 2 days. Waste of money. Customer service was unhelpful.",
            "It's okay, does what it says. Nothing special but gets the job done. Fair price."
        ]
        
        for i, review in enumerate(sample_reviews, 1):
            print(f"\n--- Review {i} Analysis ---")
            analysis = review_chain.invoke({"review_text": review})
            print(f"Sentiment: {analysis['sentiment']}")
            print(f"Rating: {analysis['rating']}/5 stars")
            print(f"Recommendation: {analysis['recommendation']}")
        
        # 3. Custom String Parser
        quote_chain = string_manipulation_parser()
        
        topics = ["success", "learning", "perseverance"]
        print(f"\n💬 Motivational Quotes:")
        print("=" * 25)
        
        for topic in topics:
            quote = quote_chain.invoke({"topic": topic})
            print(f"📝 {topic.title()}: {quote}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure your API key is valid and you have credits")

if __name__ == "__main__":
    main()