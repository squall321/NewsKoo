import { NavLink, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Articles from './pages/Articles';
import { useHealthCheck } from './hooks/useHealthCheck';

const App = () => {
  const { status, message } = useHealthCheck();

  return (
    <div>
      <nav className="navbar">
        <NavLink to="/" end className={({ isActive }) => (isActive ? 'active' : '')}>
          Home
        </NavLink>
        <NavLink to="/articles" className={({ isActive }) => (isActive ? 'active' : '')}>
          Articles
        </NavLink>
      </nav>

      <div className={`health-banner ${status}`}>
        {status === 'loading' && 'Checking API health...'}
        {status === 'ok' && `API healthy: ${message}`}
        {status === 'error' && `API issue: ${message}`}
      </div>

      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/articles" element={<Articles />} />
        </Routes>
      </main>
    </div>
  );
};

export default App;
