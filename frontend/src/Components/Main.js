import React, {Component} from 'react';
import {Switch, Route} from 'react-router-dom'
import LandingPage from './Landing'
import ErrorPage from './404Page'

class Main extends Component{
  render(){
    return(
      <main>
        <Switch>
          <Route exact path='/' component={LandingPage}/>
          <Route exact path='/Home' component={LandingPage}/>
          <Route path='*' component={ErrorPage}/>
        </Switch>
      </main> 
    )
  }
}

export default Main