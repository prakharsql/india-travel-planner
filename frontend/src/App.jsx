import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Chatbot from './components/Chatbot';
import Home from './pages/Home';
import CityPage from './pages/CityPage';
import AIPlanner from './pages/AIPlanner';
import ItineraryPage from './pages/ItineraryPage';
import ExplorePage from './pages/ExplorePage';
import AboutPage from './pages/AboutPage';

export default function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/city/:id" element={<CityPage />} />
        <Route path="/planner" element={<AIPlanner />} />
        <Route path="/planner/:cityId" element={<AIPlanner />} />
        <Route path="/itinerary" element={<ItineraryPage />} />
        <Route path="/explore" element={<ExplorePage />} />
        <Route path="/about" element={<AboutPage />} />
      </Routes>
      <Chatbot />
    </BrowserRouter>
  );
}
