import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import Login from './components/Login';
import Register from './components/Register';
import './App.css';

const ProtectedRoute = ({ children }) => {
    const token = localStorage.getItem('token');
    if (!token) {
        return <Navigate to="/login" replace />;
    }
    return children;
};

function App() {
    return (
        <Router>
            <div className="app-container">
                <header>
                    <div>
                        <h1>AUTONOMOUS ANTIGRAVITY</h1>
                        <span style={{ color: '#94a3b8', fontSize: '0.9rem' }}>Simulation & Learning Platform</span>
                    </div>
                    <div>
                        <span className="status-badge status-success">System Online</span>
                    </div>
                </header>

                <main>
                    <Routes>
                        <Route path="/login" element={<Login />} />
                        <Route path="/register" element={<Register />} />
                        <Route
                            path="/"
                            element={
                                <ProtectedRoute>
                                    <Dashboard />
                                </ProtectedRoute>
                            }
                        />
                    </Routes>
                </main>
            </div>
        </Router>
    );
}

export default App;
