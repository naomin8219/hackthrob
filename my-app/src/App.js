import Homepage from './components/homepage_component/homepage';
import Polaroid from './components/polaroid_component/polaroid';
import Survey from './components/survey_component/survey';
import{BrowserRouter as Router, Route, Link, Switch} from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Homepage />
      <Router>
        <Switch>
          <Route exact path="/">
            <Polaroid />
          </Route>
          <Route path="/survey">
            <Survey />
          </Route>
          <Route path="/date">
            <div>Insert Date component here</div>
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
