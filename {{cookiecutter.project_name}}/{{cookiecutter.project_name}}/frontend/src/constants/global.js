// Global constants

if (process.env.NODE_ENV === 'production') {
  export const BASE_URL = 'http://{{cookiecutter.domain_name}}:8000/'
} else {
  export const BASE_URL = 'http://{{cookiecutter.domain_name}}:8000/'
}
