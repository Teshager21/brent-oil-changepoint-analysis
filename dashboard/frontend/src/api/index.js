import axios from 'axios';

const API_BASE = 'http://localhost:5000/api';

export const fetchPrices = () => axios.get(`${API_BASE}/prices`);
export const fetchChangePoints = () => axios.get(`${API_BASE}/change-points`);
