import os
import argparse
import sys

from prompts import system_prompt
from call_function import available_functions
from call_function import call_function
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("api key not found")

client = genai.Client(api_key=api_key)


#run the parser
parser = argparse.ArgumentParser(description="MiniAgent")
parser.add_argument("prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true",help="Enable verbose output")
args = parser.parse_args()

#prompt
prompt = args.prompt

#final response indicator
final_response = False

#stored user messages
messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

#feedback loop
for _ in range(20):

    # test the response from the model
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt),
    )

    #get the model's responses to the last prompt and add it to the messages list
    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    metadata = response.usage_metadata

    if not metadata:
        raise RuntimeError("there was no metadata found in the response, probably failure of API")


    if args.verbose:
        #printing prompt
        print(f"User prompt: {prompt}")


        #printing token stats
        print(f"Prompt tokens: {metadata.prompt_token_count}")
        print(f"Response tokens: {metadata.candidates_token_count}")


    #process and print function calls
    if response.function_calls:
        function_results = []
        for call in response.function_calls:
            function_call_result = call_function(call, args.verbose)

            if len(function_call_result.parts) < 1:
                raise Exception("function_call_result shouldn't have an empty list in parts")
            
            if not function_call_result.parts[0].function_response:
                raise Exception("function_call_result.parts[0].function_response shouldn't be None")
            
            if not function_call_result.parts[0].function_response.response:
                raise Exception("actual funciton result shouldn't be None")
            
            print(f"Calling function: {call.name}")
            function_results.append(function_call_result.parts[0])

            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

        #append the function results to the messages list for the feedback loop   
        messages.append(types.Content(role="user", parts=function_results))
    else:
        #print response and break the feedback loop. we're done
        print(f"Final response: \n{response.text}")
        final_response = True
        break

if not final_response:  
    #we had more iterations than the maximum
    print(f"Error: maximum iterations in the feedback loop reached")
    sys.exit()

            





"""def main():
    print("Hello from miniagent!")


if __name__ == "__main__":
    main()"""
