
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

   print(f"@@@ completions is a {type(completions)} of length {len(completions)}, kwargs={kwargs}, a {type(kwargs)}, haiku_reward_v2_count={haiku_reward_v2_count}")
   haiku_reward_v2_count = haiku_reward_v2_count + 1

   # Get the 'content' field of the first completion
   contents = [completion[0]["content"] for completion in completions]

   # Calculate the reward for all completions
   return [-abs(17 - syllables.estimate(content)) for content in contents]

