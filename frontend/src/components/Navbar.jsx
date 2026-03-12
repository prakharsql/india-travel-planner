import { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);
  const location = useLocation();

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener('scroll', onScroll);
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  useEffect(() => {
    setMenuOpen(false);
  }, [location]);

  const isActive = (path) => location.pathname === path ? 'active' : '';

  return (
    <nav className={`navbar ${scrolled ? 'scrolled' : ''}`}>
      <Link to="/" className="navbar-logo">
        <span>🇮🇳</span>
        India Travel Planner
      </Link>
      <ul className={`navbar-links ${menuOpen ? 'open' : ''}`}>
        <li><Link to="/" className={isActive('/')}>Home</Link></li>
        <li><Link to="/explore" className={isActive('/explore')}>Explore</Link></li>
        <li><Link to="/planner" className={isActive('/planner')}>AI Planner</Link></li>
        <li><Link to="/about" className={isActive('/about')}>About</Link></li>
      </ul>
      <button
        className="navbar-hamburger"
        onClick={() => setMenuOpen(!menuOpen)}
        aria-label="Toggle menu"
      >
        <span></span>
        <span></span>
        <span></span>
      </button>
    </nav>
  );
}
