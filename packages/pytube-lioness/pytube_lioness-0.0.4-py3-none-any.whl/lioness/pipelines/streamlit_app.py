from pathlib import Path
from typing import Any, Tuple

import streamlit as st

from lioness.nodes.download_and_merge import _download_and_merge


def get_user_inputs() -> Tuple[str, str, str, str]:
    """Get user inputs for the YouTube URL and file paths."""
    st.title("YouTube Video and Audio Downloader")

    video_url = st.text_input("YouTube Video URL")
    path_dir_video = st.text_input("Path to save video file", "./data/video")
    path_dir_audio = st.text_input("Path to save audio file", "./data/audio")
    path_dir_combined = st.text_input("Path to save combined file", "./data/combined")

    return video_url, path_dir_video, path_dir_audio, path_dir_combined


def validate_inputs(
    video_url: str, path_dir_video: str, path_dir_audio: str, path_dir_combined: str
) -> bool:
    """Validate the user inputs."""
    if not video_url:
        st.error("Please provide a YouTube video URL.")
        return False
    if not path_dir_video:
        st.error("Please provide a path to save the video file.")
        return False
    if not path_dir_audio:
        st.error("Please provide a path to save the audio file.")
        return False
    if not path_dir_combined:
        st.error("Please provide a path to save the combined file.")
        return False
    return True


def download_and_merge_video(
    video_url: str, path_dir_video: str, path_dir_audio: str, path_dir_combined: str
) -> None:
    """Download and merge the video and audio streams."""
    download_progress_bar = st.progress(0)
    download_status_text = st.empty()

    def update_download_progress(downloaded: Any, total: Any) -> None:
        progress = downloaded / total
        download_progress_bar.progress(progress)
        download_status_text.text(f"Downloading: {progress * 100:.2f}%")

    try:
        _download_and_merge(
            video_url,
            Path(path_dir_video),
            Path(path_dir_audio),
            Path(path_dir_combined),
            progress_callback=update_download_progress,
        )
        st.success("Download and merge complete!")
    except Exception as e:
        st.error(f"An error occurred: {e}")


def main() -> None:
    """Main function to run the Streamlit app."""
    video_url, path_dir_video, path_dir_audio, path_dir_combined = get_user_inputs()

    if st.button("Download and Merge"):
        if validate_inputs(
            video_url, path_dir_video, path_dir_audio, path_dir_combined
        ):
            download_and_merge_video(
                video_url, path_dir_video, path_dir_audio, path_dir_combined
            )


if __name__ == "__main__":
    main()
