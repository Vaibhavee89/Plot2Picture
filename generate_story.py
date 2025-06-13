import openai
import json
import time
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

# Step 1: Input short story
short_story = """
A young girl finds a mysterious map in her grandmother's attic 
and sets out on an adventure to find a hidden treasure deep in 
the forest. 
"""








def generate_storyboard(story_text):
    global short_story
    short_story = story_text
    
    # Step 2: Prompt GPT to break story into scenes
    scene_prompt = f"""
    Given the story: "{short_story}", break it into exactly 10 progressive scenes.
    Return a JSON array of 10 objects with:
    - scene_number (1–10)
    - storyline (1-2 sentences)
    - image_prompt (short description of the scene for image generation)
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a creative storyboard generator."},
            {"role": "user", "content": scene_prompt}
        ]
    )

    storyboard_data = json.loads(response.choices[0].message.content)

    # Step 3: Generate image URLs using DALL·E
    for scene in storyboard_data:
        try:
            image_response = client.images.generate(
                model = "dall-e-3",
                prompt=scene["image_prompt"],
                n=1,
                size="1024x1024",
            )
            scene["image_url"] = image_response.data[0].url
            print(f"\nScene {scene['scene_number']} generated successfully:")
            print(f"Prompt: {scene['image_prompt']}")
            print(f"Image URL: {scene['image_url']}")
            # time.sleep(1)  # rate limit safety
        except Exception as e:
            scene["image_url"] = "https://example.com/fallback.jpg"
            print(f"\nImage generation failed for scene {scene['scene_number']}:")
            print(f"Error: {e}")
            print(f"Prompt that failed: {scene['image_prompt']}")

    return storyboard_data

if __name__ == "__main__":
    storyboard = generate_storyboard(short_story)
    with open("storyboard_with_images.json", "w") as f:
        json.dump(storyboard, f, indent=2)
    print("Storyboard generation complete. Check 'storyboard_with_images.json'")
