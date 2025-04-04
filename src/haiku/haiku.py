
from typing import Dict
import syllables


def haiku_reward(completions: list[list[Dict[str, str]]], **kwargs) -> float:
   """
   Reward the completion with the closest number of syllables to 17.

   This simulates a reward that promotes the solution that is closest to a Haiku poem.
   """

   # Get the 'content' field of the first completion
   contents = [completion[0]["content"] for completion in completions]

   # Calculate the reward for all completions
   return [-abs(17 - syllables.estimate(content)) for content in contents]

haiku_reward_v2_count = 0

def haiku_reward_v2(completions: list[list[Dict[str, str]]], **kwargs) -> float:
   """
   Reward the completion with the closest number of syllables to 17.

   This simulates a reward that promotes the solution that is closest to a Haiku poem.
   """

   # completions is a list of length 16.
   # kwargs is a dict with keys 'prompts', 'problem', 'solution', 'answer', 'problem_type',
   # 'question_type', 'source', 'uuid', 'is_reasoning_complete', 'generations', 'correctness_math_verify',
   # 'correctness_llama', 'finish_reasons', and 'correctness_count'.

   # haiku_reward_v2_count goes up to (EXPERIMENT_MAX_STEPS * 4) - 1

   def myfunc(n):
      return str(len(n))

   global haiku_reward_v2_count
   # print(f"@@@ ecs completions is a {type(completions)} of length {len(completions)}, kwargs is a {type(kwargs)}, haiku_reward_v2_count={haiku_reward_v2_count}")
   kwargs_copy = {k: kwargs[k] for k in kwargs.keys() - {'Prompts', 'prompts', 'solution'}}
   # print(f"@@@ ecs completions shape is {','.join(map(myfunc, completions))}, kwargs={kwargs}, haiku_reward_v2_count={haiku_reward_v2_count}")
   print(f"@@@ ecs kwargs={kwargs_copy}, haiku_reward_v2_count={haiku_reward_v2_count}")
   # print(f"@@@ ecs completions[0] is a {type(completions[0])} of length {len(completions[0])}, kwargs has keys {list(kwargs.keys())}, haiku_reward_v2_count={haiku_reward_v2_count}")
   haiku_reward_v2_count = haiku_reward_v2_count + 1

   # Get the 'content' field of the first completion
   contents = [completion[0]["content"] for completion in completions]

   # Calculate the reward for all completions
   return [-abs(17 - syllables.estimate(content)) for content in contents]

