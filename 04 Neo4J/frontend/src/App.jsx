
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/Auth/Login';
import Signup from './components/Auth/Signup';
import EditProfile from './components/User/EditProfile';
import DeleteAccount from './components/User/DeleteAccount';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          
          <Route path="/login" component={Login} />
          <Route path="/signup" component={Signup} />
          <Route path="/edit-profile" component={EditProfile} />
          <Route path="/delete-account" component={DeleteAccount} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
