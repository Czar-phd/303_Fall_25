import wikipedia
from concurrent.futures import ThreadPoolExecutor
import time

print("=" * 70)
print("PART A: Sequential Download")
print("=" * 70)

topics_sequential = wikipedia.search("generative artificial intelligence")

start_time_sequential = time.perf_counter()

for topic in topics_sequential:
    try:
        page = wikipedia.page(topic, auto_suggest=False)
        
        title = page.title
        references = page.references
        
        references_str = "\n".join(references)
        
        safe_title = title.replace("/", "_").replace("\\", "_")
        filename = f"{safe_title}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(references_str)
        
        print(f"Saved references for '{title}'")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"DisambiguationError for topic '{topic}': {e}")
    except wikipedia.exceptions.PageError as e:
        print(f"PageError for topic '{topic}': {e}")
    except Exception as e:
        print(f"Error processing topic '{topic}': {e}")

end_time_sequential = time.perf_counter()

print(f"\nSequential Execution Time: {end_time_sequential - start_time_sequential:.2f} seconds")

print("\n" + "=" * 70)
print("PART B: Concurrent Download")
print("=" * 70)

def wiki_dl_and_save(topic):
    """
    Retrieve Wikipedia page for a topic, extract references, and save to file.
    """
    try:
        page = wikipedia.page(topic, auto_suggest=False)
        
        title = page.title
        references = page.references
        
        references_str = "\n".join(references)
        
        safe_title = title.replace("/", "_").replace("\\", "_")
        filename = f"{safe_title}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(references_str)
        
        print(f"Saved references for '{title}'")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"DisambiguationError for topic '{topic}': {e}")
    except wikipedia.exceptions.PageError as e:
        print(f"PageError for topic '{topic}': {e}")
    except Exception as e:
        print(f"Error processing topic '{topic}': {e}")

topics_concurrent = wikipedia.search("generative artificial intelligence")

start_time_concurrent = time.perf_counter()
with ThreadPoolExecutor() as executor:
    executor.map(wiki_dl_and_save, topics_concurrent)
end_time_concurrent = time.perf_counter()

print(f"\nConcurrent Execution Time: {end_time_concurrent - start_time_concurrent:.2f} seconds")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"Sequential Time: {end_time_sequential - start_time_sequential:.2f} seconds")
print(f"Concurrent Time: {end_time_concurrent - start_time_concurrent:.2f} seconds")
speedup = (end_time_sequential - start_time_sequential) / (end_time_concurrent - start_time_concurrent)
print(f"Speedup: {speedup:.2f}x")
