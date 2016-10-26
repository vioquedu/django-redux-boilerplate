import * as ActionTypes from '../actions'
import merge from 'lodash/merge'
import { routerReducer as routing } from 'react-router-redux'
import { combineReducers } from 'redux'
import auth  from './auth.js'

// Updates the pagination data for different actions.
const rootReducer = combineReducers({
    auth,
    routing
})

export default rootReducer
