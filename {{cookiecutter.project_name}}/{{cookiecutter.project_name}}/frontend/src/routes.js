import React from 'react'
import { Route, IndexRoute } from 'react-router'
import AuthenticatedApp from './containers/AuthenticatedApp'
import SignIn from './containers/SignIn'
import Logout from './components/auth/Logout'
import Main from './components/Main'
import { requireAuthentication } from './components/auth/AuthenticatedComponent'

export default (
  <Route path="/" component={AuthenticatedApp}>
	<IndexRoute component={requireAuthentication(Main)}  />
	<Route path="signin/" component={SignIn} />
	<Route path="logout-page/" component={Logout} />
  </Route>
)
