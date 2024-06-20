from functools import wraps
from contextvars import ContextVar

_goonie_context = ContextVar('goonie_context',
                             default=None)

def goonie(llm=None,
           iam=None,
           tools=[],
           prompts={},
           thread_safe=True):

    tools_dict = {tool.__name__: tool for tool in tools}

    def decorator(func):
        nonlocal iam
        if iam is None:
            iam = f"{func.__module__}.{func.__name__}"

        @wraps(func)
        def wrapper(*args, **kwargs):
            context_token = None

            if thread_safe:

                # init goonie context for the current thread
                context_token = _goonie_context.set({
                    'llm': llm,
                    'iam': iam,
                    'tools': tools_dict,
                    'prompts': prompts
                })

            else:
                # (!) update globals in non-thread-safe manner
                func_globals = func.__globals__
                func_globals.update({'llm': llm, 'iam': iam, 'tools': tools_dict, 'prompts': prompts})

            try:
                # rock & roll
                return func(*args, **kwargs)
            finally:
                if thread_safe:
                    # reset the context to previous state
                    _goonie_context.reset(context_token)
                else:
                    # clen up globals
                    for key in ['llm', 'iam', 'tools', 'prompts']:
                        func_globals.pop(key, None)

        return wrapper
    return decorator

def goontext():
    context = _goonie_context.get()
    if context is None:
        return None  # an empy map maybe?
    return (context['llm'],
            context['tools'],
            context['iam'],
            context['prompts'])
