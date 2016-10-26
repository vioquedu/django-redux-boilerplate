import { CALL_API, Schemas } from '../middleware/api'
import { browserHistory } from 'react-router';
import { LOGIN_URL } from '../constants/auth_constants'
import { LOGIN_REQUEST, LOGIN_SUCCESS, LOGIN_FAILURE } from '../constants/auth_constants'
import { LOGOUT_REQUEST } from '../constants/auth_constants'
import { UPDATE_LOGIN_FORM } from '../constants/auth_constants'



// Returns cookie value
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
	var cookies = document.cookie.split(';');
	for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
		var cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		break;
            }
	}
    }
    return cookieValue;
}


// UPDATE LOGIN FORM
export function update_login_form(value, key){
    return {
	type: UPDATE_LOGIN_FORM,
	value: value,
	key: key
    }
}

// LOGIN ACTIONS
function login_request() {
    return {
	type: LOGIN_REQUEST,
	isFetching: true
    }
}

function login_success(token) {
    return {
	type: LOGIN_SUCCESS,
	isFetching: false,
	isAuthenticated: true,
	token: token,
	err: null
    }
}

function login_failure(err) {
    return {
	type: LOGIN_FAILURE,
	isAuthenticated: false,
	isFetching: false,
	err: err
    }
}

// Log in user
export function loginUser(creds, redirect="/") {
    // Get csrf token
    let csrf_token = getCookie('csrftoken')

    // Build body data
    let body = new FormData()
    body.append('username', creds.username)
    body.append('password', creds.password)
    body.append('csrfmiddlewaretoken', csrf_token)

    // Build request 
    let config = {
	method: 'POST',
	body: body
    }
    // Get url
    let URL = LOGIN_URL

    // Dispatch login
    return dispatch => {
	dispatch(login_request())
	return fetch(URL, config)
	    .then(response =>
		  response.json().then(user => ({ user, response }))
		 ).then(({ user, response }) =>  {
		     if (!response.ok) {
			 // If there was a problem, we want to
			 // dispatch the error condition
			 dispatch(login_failure(user))
			 return Promise.reject(user)
		     } else {
			 // If login was successful, set the token in local storage
			 localStorage.setItem('id_token', user.token)
			 // Dispatch the success action
			 dispatch(login_success(user.token))
			 // Redirect
			 browserHistory.push(redirect)
		     }
		 }).catch(err => console.log("Error: ", err))
		     }
}


/// LOGOUT ACTIONS
function logout_request() {
    return {
	type: LOGOUT_REQUEST,
	isAuthenticated: false,
	payload: {},
	login_form: {username: '', password: ''}
    }
}


export function logoutUser() {
    return dispatch => {
	// Remove token
	localStorage.removeItem('id_token')
	// Dispatch logout request
	dispatch(logout_request())
	browserHistory.push("logout-page/")
    }
}
