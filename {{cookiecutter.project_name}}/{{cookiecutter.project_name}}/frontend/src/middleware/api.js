import { Schema, arrayOf, normalize } from 'normalizr'
import { camelizeKeys } from 'humps'
import 'isomorphic-fetch'
import {BASE_URL} from '../constants/global'

function callApi(endpoint, authenticated) {
  let token = localStorage.getItem('id_token') || null
  let config = {}

  if(authenticated) {
    if(token){
      config = {headers: {Authorization: "JWT " + `${token}`}}
    } else {
      throw "No token saved"
    }
  }

  return fetch(BASE_URL + endpoint, config)
    .then(response => response.text().then(text => ({text, response}))
    ).then(({ text, response }) => {
      if(!response.ok){
	return Promise.rejext(text)
      }
      return JSON.parse(text)
    }).catch(err => console.lot(err))
}


// Action key that carries API call info interpreted by this Redux middleware.
export const CALL_API = Symbol('Call API')

// A Redux middleware that interprets actions with CALL_API info specified.
// Performs the call and promises when such actions are dispatched.
export default store => next => action => {
  const callAPI = action[CALL_API]
  if (typeof callAPI === 'undefined') {
    return next(action)
  }

  let { endpoint, authenticated } = callAPI
  const { schema, types } = callAPI

  if (typeof endpoint === 'function') {
    endpoint = endpoint(store.getState())
  }

  if (typeof endpoint !== 'string') {
    throw new Error('Specify a string endpoint URL.')
  }
  /* if (!schema) {
   *   throw new Error('Specify one of the exported Schemas.')
   * }*/
  if (!Array.isArray(types) || types.length !== 3) {
    throw new Error('Expected an array of three action types.')
  }
  if (!types.every(type => typeof type === 'string')) {
    throw new Error('Expected action types to be strings.')
  }

  function actionWith(data) {
    const finalAction = Object.assign({}, action, data)
    delete finalAction[CALL_API]
    return finalAction
  }

  const [ requestType, successType, failureType ] = types
  next(actionWith({ type: requestType }))

  //return callApi(endpoint, schema).then(
  return callApi(endpoint, authenticated).then(
    response => next(actionWith({
      response,
      type: successType
    })),
    error => next(actionWith({
      type: failureType,
      error: error.message || 'Something bad happened'
    }))
  )
}
