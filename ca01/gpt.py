import openai

class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey=apikey
        # Set up the OpenAI API client
        openai.api_key = apikey #os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def __getResponse(self,prompt):
        ''' Generate a GPT response
         returns a tuple with the response, and a status code. 0 if success, 1 if error '''
        try:
            completion = openai.Completion.create(
                engine=self.model_engine,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.8,
            )

            response = completion.choices[0].text
        except Exception:
            return "Server side error, please try again later. ", 1
        return response, 0
    
    # Archer's prompt
    def archers_prompt(self, prompt):
        return self.__getResponse("Write a story about a superhero whose power is to turn into a {} whenever they sneeze.".format(prompt))

    # Paras's prompt
    def paras_prompt(self, prompt):
        return self.__getResponse("which tv show or movie are they form {}".format(prompt))


    # Kelden's prompt
    
    # Efren's prompt
    def efren_prompt(self,prompt):
        response = self.__getResponse(prompt)
        return prompt,response

    # Samir's prompt

if __name__=='__main__':
    import os
    g = GPT(os.environ.get("APIKEY"))
    print(g._GPT__getResponse("what does openai's GPT stand for?"))
