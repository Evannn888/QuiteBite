import { render, screen } from '@testing-library/react';
import App from './App';

test('renders QuickBites navbar brand', () => {
  render(<App />);
  const brandElement = screen.getByText(/QuickBites/i);
  expect(brandElement).toBeInTheDocument();
});
