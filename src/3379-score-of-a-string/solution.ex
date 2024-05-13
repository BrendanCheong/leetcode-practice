defmodule Solution do
  @spec score_of_string(s :: String.t) :: integer
  def score_of_string(s) do
    s 
    |> String.graphemes() # turn string into list of characters
    |> Enum.map(&char_code/1) # turn each character into ASCII number
    |> Enum.chunk_every(2, 1, :discard)  # Creates overlapping pairs of characters
    |> Enum.map(fn [a, b] -> abs(a - b) end) # Map over the absolute differences
    |> Enum.sum() # Sum up differences
  end

  # Function to get ASCII value of a character
  defp char_code(char) do
    :binary.at(char, 0)
  end
end
