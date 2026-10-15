const btn = document.querySelector("#toggle")
btn.addEventListener("click", function() {document.body.classList.toggle("dark")})

const input = document.querySelector("#book")
const list = document.querySelector("#list")
const addButton = document.querySelector("#add-btn")
addButton.addEventListener("click", function() {
    input.reportValidity()
    if (input.value && input.validity.valid) {
        const li = document.createElement("li")
        li.textContent = input.value
        li.addEventListener("click", function() {
            li.remove()
        })
        list.appendChild(li)
        input.value = ""
    }
})