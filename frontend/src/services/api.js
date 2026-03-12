import axios from 'axios';

const API_BASE = '/api';

const api = axios.create({
  baseURL: API_BASE,
  headers: { 'Content-Type': 'application/json' },
});

// ── Cities ──
export const getCities = (search = '') =>
  api.get('/cities/', { params: search ? { search } : {} }).then(r => r.data);

export const getCityDetail = (id) =>
  api.get(`/cities/${id}/`).then(r => r.data);

export const getCityPlaces = (id) =>
  api.get(`/cities/${id}/places/`).then(r => r.data);

export const getCityFoods = (id) =>
  api.get(`/cities/${id}/foods/`).then(r => r.data);

// ── AI Itinerary ──
export const generateItinerary = (cityId, numDays, budget, interests) =>
  api.post('/generate-ai-itinerary/', {
    city_id: cityId,
    num_days: numDays,
    budget,
    interests,
  }).then(r => r.data);

// ── PDF Download ──
export const downloadPDF = (cityId, itinerary) =>
  api.post('/download-itinerary-pdf/', {
    city_id: cityId,
    itinerary,
  }, { responseType: 'blob' }).then(r => {
    const url = window.URL.createObjectURL(new Blob([r.data]));
    const link = document.createElement('a');
    link.href = url;
    link.download = `itinerary.pdf`;
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.URL.revokeObjectURL(url);
  });

// ── Weather ──
export const getWeather = (city) =>
  api.get('/weather/', { params: { city } }).then(r => r.data);

// ── Chatbot ──
export const sendChatMessage = (message, cityContext = '') =>
  api.post('/chat/', { message, city_context: cityContext }).then(r => r.data);

export default api;
