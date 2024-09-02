const scriptURL = 'https://script.google.com/macros/s/AKfycbyq4i4zPVn-tlQC1-i110Tp8gmIjaw4ddk8gzP_W9MaW9IU8LqTzBcItMB24s_hkxrbXw/exec'


const form = document.forms['contact-form']


form.addEventListener('submit', e => {
  e.preventDefault()
  fetch(scriptURL, { method: 'POST', body: new FormData(form)})
  .then(response => alert("Thank you! your form is submitted successfully." ))
  .then(() => { window.location.reload(); })
  .catch(error => console.error('Error!', error.message))
})
