import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import SearchForm from './SearchForm';

describe('SearchForm Component', () => {
  const mockOnSearch = jest.fn();

  beforeEach(() => {
    mockOnSearch.mockClear();
  });

  test('renders search form elements', () => {
    render(<SearchForm onSearch={mockOnSearch} />);
    
    // Check if all form elements are present
    expect(screen.getByPlaceholderText(/search/i)).toBeInTheDocument();
    expect(screen.getByText(/ingredients/i)).toBeInTheDocument();
    expect(screen.getByText(/tags/i)).toBeInTheDocument();
    expect(screen.getByText(/difficulty/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /search/i })).toBeInTheDocument();
  });

  test('handles search submission', () => {
    render(<SearchForm onSearch={mockOnSearch} />);
    
    // Fill in the form
    const searchInput = screen.getByPlaceholderText(/search/i);
    fireEvent.change(searchInput, { target: { value: 'chicken' } });

    const ingredientsInput = screen.getByLabelText(/ingredients/i);
    fireEvent.change(ingredientsInput, { target: { value: 'rice,chicken' } });

    const tagsInput = screen.getByLabelText(/tags/i);
    fireEvent.change(tagsInput, { target: { value: 'dinner,healthy' } });

    const difficultySelect = screen.getByLabelText(/difficulty/i);
    fireEvent.change(difficultySelect, { target: { value: 'medium' } });

    // Submit the form
    const searchButton = screen.getByRole('button', { name: /search/i });
    fireEvent.click(searchButton);

    // Check if onSearch was called with correct parameters
    expect(mockOnSearch).toHaveBeenCalledWith({
      query: 'chicken',
      ingredients: ['rice', 'chicken'],
      tags: ['dinner', 'healthy'],
      difficulty: 'medium'
    });
  });

  test('handles empty search submission', () => {
    render(<SearchForm onSearch={mockOnSearch} />);
    
    // Submit empty form
    const searchButton = screen.getByRole('button', { name: /search/i });
    fireEvent.click(searchButton);

    // Check if onSearch was called with empty parameters
    expect(mockOnSearch).toHaveBeenCalledWith({
      query: '',
      ingredients: [],
      tags: [],
      difficulty: ''
    });
  });

  test('validates input fields', () => {
    render(<SearchForm onSearch={mockOnSearch} />);
    
    const searchInput = screen.getByPlaceholderText(/search/i);
    fireEvent.change(searchInput, { target: { value: '   ' } });
    
    const searchButton = screen.getByRole('button', { name: /search/i });
    fireEvent.click(searchButton);

    // Should trim whitespace
    expect(mockOnSearch).toHaveBeenCalledWith(expect.objectContaining({
      query: ''
    }));
  });
}); 