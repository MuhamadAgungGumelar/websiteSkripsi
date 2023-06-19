const loading = document.getElementById("loading-container")
loading.style.display = "none";


document.getElementById("button-submit").addEventListener("click", function(){
    loading.style.display = "block";
});