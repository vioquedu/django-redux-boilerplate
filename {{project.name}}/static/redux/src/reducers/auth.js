import { UPDATE_LOGIN_FORM } from '../constants/auth_constants'
import { LOGIN_REQUEST, LOGIN_SUCCESS, LOGIN_FAILURE } from '../constants/auth_constants'
import { LOGOUT_REQUEST } from '../constants/auth_constants'
import jwt_decode from 'jwt-decode'


function getInitialAuthState() {
    // Get token 
    var token = localStorage.getItem('id_token')
    var isAuthenticated = false
    var payload = {}
    if(token!=null) {
	try  {
	    var token_info = jwt_decode(token)
	    var now = Date.now()/1000
	    if(now < token_info.exp) {
		payload = token_info
		isAuthenticated = true
	    }
	}catch(err) {
	    console.log(err)
	}
    }
	
    return { 
	login_form: {
	    username: '',
	    password: ''
	},
	isFetching: false,
	isAuthenticated: isAuthenticated,
	payload: payload,
	error: null,
	token: token
    }
}

// Auth reducer
export default function auth(state = getInitialAuthState(), action) {
    switch(action.type) {

	// Update login form
    case UPDATE_LOGIN_FORM:
	var form = state.login_form;
	form[action.key] = action.value;
	return Object.assign({}, state, {
	    login_form: form
	});
	/////////////////////
	// Login actions
    case LOGIN_REQUEST:
	return Object.assign({}, state, {
	    isFetching: action.isFetching
	});
    case LOGIN_SUCCESS:
	return Object.assign({}, state, {
	    isFetching: action.isFetching,
	    isAuthenticated: action.isAuthenticated,
	    payload: jwt_decode(action.token),
	    token: action.token,
	    error: action.err
	});
    case LOGIN_FAILURE:
	return Object.assign({}, state, {
	    login_form: {username: '', password: ''},
	    isFetching: action.isFetching,
	    isAuthenticated: action.isAuthenticated,
	    token: undefined,
	    error: action.err
	});
	// Logout actions
    case LOGOUT_REQUEST:
	return Object.assign({}, state, {
	    isAuthenticated: action.isAuthenticated,
	    payload: action.payload,
	    login_form: action.login_form,
	    token: undefined,
	});
    default:
	return state;
    }
}
