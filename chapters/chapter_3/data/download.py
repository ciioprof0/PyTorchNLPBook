#
# CREDIT: https://stackoverflow.com/a/39225039
#

"""Download a file from Google Drive."""

import requests

def progress_bar(some_iter):
    """Wrap an iterable with a progress bar if tqdm is installed."""
    try:
        from tqdm import tqdm
        return tqdm(some_iter)
    except ModuleNotFoundError:
        return some_iter

def download_file_from_google_drive(id, destination):
    """Download a file from Google Drive."""
    print("Trying to fetch {}".format(destination))

    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        """Save the response content to a file."""
        chunk_size = 32768

        with open(destination, "wb") as f:
            for chunk in progress_bar(response.iter_content(chunk_size)):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    url = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(url, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(url, params = params, stream = True)

    save_response_content(response, destination)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python download.py drive_file_id destination_file_path")
    else:
        # TAKE ID FROM SHAREABLE LINK
        file_id = sys.argv[1]
        # DESTINATION FILE ON YOUR DISK
        destination = sys.argv[2]
        download_file_from_google_drive(file_id, destination)
