<div style="display: flex; align-items: center;">
  <a href="https://huggingface.co/syubraj/sentence_similarity_nepali_v2">
    <img alt="Sentence-Transformers Huggingface" src="https://huggingface.co/front/assets/huggingface_logo.svg" style="width: 50px; height: auto;">
  </a>
  <span id="downloads" style="margin-left: 10px;">Downloads: Loading...</span>
</div>

<script>
  // Fetch the number of downloads from Hugging Face API
  async function fetchDownloads() {
    const response = await fetch('https://huggingface.co/api/models/syubraj/sentence_similarity_nepali_v2');
    const data = await response.json();
    const downloads = data.downloads; // Extracting the downloads count

    // Update the HTML with the dynamic value
    document.getElementById('downloads').textContent = `Downloads: ${downloads.toLocaleString()}`;
  }

  // Call the function to fetch and display downloads
  fetchDownloads();
</script>
