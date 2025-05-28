document.getElementById('search-form').addEventListener('submit', function(event) {
  event.preventDefault();

  const query = document.getElementById('query').value.trim();
  if (query === '') return;

  fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`)
    .then(res => res.json())
    .then(data => {
      console.log(data);
    })
    .catch(err => {
      console.error('Fetch error:', err);
    });
});