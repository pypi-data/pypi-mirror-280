import argparse, os
from dotenv import load_dotenv

import goonies.thinker as thinker
from goonies.base import goonie, goontext
from goonies.tools import color
from goonies.toolbox.web import read_url_as_text, search_web

def playground():

    llm = thinker.Claude(model_name="claude-3-haiku-20240307")
    # llm = thinker.Ollama(model_name="llama3:latest")

    print(color.GRAY_MEDIUM + f"{llm}" + color.END)

    ## TODO decide on what needs to go to the agent decorator
    ##      because:
    ##         - prompts should/might not, they need local function variables
    ##         - potentially functions? (e.g. https://platform.openai.com/docs/guides/function-calling)
    ##         - tools should not, they are functions that are imported in a module
    ##         - iam might, but will be default, and should be used to register this goonie vs. as a function local variable
    ##         - feedback should be optional and dynamic: different feedback for different function results

    @goonie(llm=llm,
            prompts={'summarize-it': "given this topic: {topic}, and these search results from the web: {results}, focus on the topic and summarize the top 10 most important news items given the topic"})
    def read_news(topic):

        llm, _, iam, prompts = goontext()

        results = search_web(topic, results_as="json")

        prompt = prompts['summarize-it'].format(topic=topic,
                                                results=results)
        news = llm.think(prompt=prompt,
                         who=iam)
        return {'news': news}

    @goonie(llm=llm,
            prompts={'main points': 'summarize the main points in this paper',
                     'eli5':        'explain this paper like I\'m 5 years old',
                     'issues':      'summarize issues that you can identify with ideas in this paper'})
    def summarize_paper(url):

        llm, _, _, prompts = goontext()

        paper = read_url_as_text(url)
        summary = llm.think(prompt=prompts['main points'] + paper,
                            who="paper reviewer")
        eli5 = llm.think(prompt=prompts['eli5'] + paper,
                         who="explain like I'm 5 years old")
        issues = llm.think(prompt=prompts['issues'] + paper,
                           who="issues with ideas in this paper")

        return {'main points': summary,
                'eli5': eli5,
                'issues': issues}

    ## "The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits"
    # summary = summarize_paper("https://arxiv.org/pdf/2402.17764")

    # print(color.GRAY_MEDIUM + f"paper summary: {summary}" + color.END)

    news = read_news("what are the latest news about \"llama.cpp\"?")

    # print(color.GRAY_MEDIUM + f"news: {news}" + color.END)


def main():

    ## ----------------------------- setup
    env_path = os.path.join(os.getcwd(), '.env')
    load_dotenv(dotenv_path=env_path)

    # args = parse_cli_arguments()

    ## ----------------------------- playground
    # brain = llm.make_brain(options=args)
    playground()

if __name__ == '__main__':
    main()
