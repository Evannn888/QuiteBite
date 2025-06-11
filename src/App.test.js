import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import App from './App';

// Mock fetch function
global.fetch = jest.fn();

describe('App Component', () => {
  beforeEach(() => {
    // Reset all mocks before each test
    fetch.mockClear();
  });

  test('renders QuickBites title', () => {
    render(<App />);
    const titleElement = screen.getByText(/QuickBites/i);
    expect(titleElement).toBeInTheDocument();
  });

  test('loads and displays recipes', async () => {
    const mockRecipes = [
      {
        id: 1,
        name: 'Test Recipe',
        description: 'Test Description',
        prep_time: 30,
        cook_time: 45,
        difficulty: 'medium'
      }
    ];

    fetch.mockImplementationOnce(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve(mockRecipes)
      })
    );

    render(<App />);
    
    // Wait for recipes to load
    await waitFor(() => {
      expect(screen.getByText('Test Recipe')).toBeInTheDocument();
    });
  });

  test('handles search functionality', async () => {
    const mockSearchResults = [
      {
        id: 2,
        name: 'Search Result Recipe',
        description: 'Search Result Description',
        prep_time: 20,
        cook_time: 30,
        difficulty: 'easy'
      }
    ];

    fetch.mockImplementationOnce(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve(mockSearchResults)
      })
    );

    render(<App />);

    // Fill in search form
    const searchInput = screen.getByPlaceholderText(/search/i);
    fireEvent.change(searchInput, { target: { value: 'chicken' } });

    // Submit search
    const searchButton = screen.getByText(/search/i);
    fireEvent.click(searchButton);

    // Wait for search results
    await waitFor(() => {
      expect(screen.getByText('Search Result Recipe')).toBeInTheDocument();
    });
  });

  test('displays error message when API fails', async () => {
    fetch.mockImplementationOnce(() =>
      Promise.reject(new Error('Failed to fetch'))
    );

    render(<App />);

    await waitFor(() => {
      expect(screen.getByText(/failed to fetch/i)).toBeInTheDocument();
    });
  });

  test('shows loading state', async () => {
    fetch.mockImplementationOnce(() =>
      new Promise(resolve => setTimeout(resolve, 100))
    );

    render(<App />);
    
    expect(screen.getByRole('status')).toBeInTheDocument();
  });
});
