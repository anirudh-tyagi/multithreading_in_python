import requests
import os
import threading
import time
import sys

def download_file(url):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Extract filename from URL or generate a fallback name
        filename = os.path.basename(url)
        if not filename:
            filename = f"download_{abs(hash(url))}.dat"  # Fallback name
        
        print(f"Downloading {url} to {filename}")
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Finished downloading {filename}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def sequential_download(urls):
    start_time = time.time()
    for url in urls:
        download_file(url)
    return time.time() - start_time

def concurrent_download(urls):
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_file, args=(url,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return time.time() - start_time

def get_urls():
    if len(sys.argv) < 2:
        print("Usage: python downloader.py <file_with_urls.txt> or <URL1> <URL2> ...")
        sys.exit(1)
    
    input_arg = sys.argv[1]
    if os.path.isfile(input_arg):
        with open(input_arg, 'r') as f:
            urls = [line.strip() for line in f.readlines() if line.strip()]
    else:
        urls = [url for url in sys.argv[1:] if url]
    
    if not urls:
        print("No valid URLs provided.")
        sys.exit(1)
    
    return urls

def main():
    urls = get_urls()
    print(f"Starting download for {len(urls)} files...")
    
    # Sequential download
    print("\n--- Sequential Download ---")
    seq_time = sequential_download(urls)
    print(f"Sequential download completed in {seq_time:.2f} seconds.")
    
    # Concurrent download
    print("\n--- Concurrent Download ---")
    con_time = concurrent_download(urls)
    print(f"Concurrent download completed in {con_time:.2f} seconds.")
    
    # Print comparison
    print("\n--- Comparison ---")
    print(f"Sequential Time: {seq_time:.2f} sec")
    print(f"Concurrent Time: {con_time:.2f} sec")
    if con_time > 0:
        print(f"Concurrent download was {seq_time / con_time:.2f}x faster!")

if __name__ == "__main__":
    main()