import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import RecipeCard from './RecipeCard';

describe('RecipeCard Component', () => {
  const mockRecipe = {
    id: 1,
    name: 'Test Recipe',
    description: 'Test Description',
    prep_time: 30,
    cook_time: 45,
    difficulty: 'medium',
    ingredients: ['ingredient1', 'ingredient2'],
    tags: ['tag1', 'tag2']
  };

  test('renders recipe information correctly', () => {
    render(<RecipeCard recipe={mockRecipe} />);
    
    // Check if all recipe information is displayed
    expect(screen.getByText('Test Recipe')).toBeInTheDocument();
    expect(screen.getByText('Test Description')).toBeInTheDocument();
    expect(screen.getByText('30 mins')).toBeInTheDocument();
    expect(screen.getByText('45 mins')).toBeInTheDocument();
    expect(screen.getByText('medium')).toBeInTheDocument();
  });

  test('displays ingredients and tags', () => {
    render(<RecipeCard recipe={mockRecipe} />);
    
    // Check if ingredients and tags are displayed
    mockRecipe.ingredients.forEach(ingredient => {
      expect(screen.getByText(ingredient)).toBeInTheDocument();
    });
    
    mockRecipe.tags.forEach(tag => {
      expect(screen.getByText(tag)).toBeInTheDocument();
    });
  });

  test('handles missing optional fields', () => {
    const minimalRecipe = {
      id: 1,
      name: 'Minimal Recipe',
      description: 'Minimal Description',
      prep_time: 30,
      cook_time: 45,
      difficulty: 'medium'
    };

    render(<RecipeCard recipe={minimalRecipe} />);
    
    // Should still render without crashing
    expect(screen.getByText('Minimal Recipe')).toBeInTheDocument();
    expect(screen.getByText('Minimal Description')).toBeInTheDocument();
  });

  test('applies correct difficulty class', () => {
    render(<RecipeCard recipe={mockRecipe} />);
    
    const difficultyBadge = screen.getByText('medium');
    expect(difficultyBadge).toHaveClass('badge', 'bg-warning');
  });

  test('displays total cooking time', () => {
    render(<RecipeCard recipe={mockRecipe} />);
    
    const totalTime = mockRecipe.prep_time + mockRecipe.cook_time;
    expect(screen.getByText(`${totalTime} mins`)).toBeInTheDocument();
  });

  test('handles different difficulty levels', () => {
    const difficulties = {
      easy: 'bg-success',
      medium: 'bg-warning',
      hard: 'bg-danger'
    };

    Object.entries(difficulties).forEach(([level, className]) => {
      const recipe = { ...mockRecipe, difficulty: level };
      render(<RecipeCard recipe={recipe} />);
      
      const difficultyBadge = screen.getByText(level);
      expect(difficultyBadge).toHaveClass('badge', className);
    });
  });

  test('formats time display correctly', () => {
    const recipe = {
      ...mockRecipe,
      prep_time: 60,
      cook_time: 90
    };

    render(<RecipeCard recipe={recipe} />);
    
    expect(screen.getByText('1 hr')).toBeInTheDocument();
    expect(screen.getByText('1 hr 30 mins')).toBeInTheDocument();
  });
}); 