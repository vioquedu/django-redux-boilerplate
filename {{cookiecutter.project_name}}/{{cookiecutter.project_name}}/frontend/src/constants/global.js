// Global constants

if (process.env.NODE_ENV === 'production') {
  var BASE_URL = 'http://{{cookiecutter.domain_name}}:8000/'
} else {
  var BASE_URL = 'http://{{cookiecutter.domain_name}}:8000/'
}
export {BASE_URL}
