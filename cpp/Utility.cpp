char get_char_immediately()
{
  // Set terminal to raw mode 
  system("stty raw"); 

  // Wait for single character 
  char input = getchar(); 

  // Reset terminal to normal "cooked" mode 
  system("stty cooked");

  return input;
}