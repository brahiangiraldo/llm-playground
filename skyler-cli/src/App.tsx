

import { ReactTerminal, TerminalContextProvider } from 'react-terminal'
import './App.css'

function App() {
  const commands = {
    help: "Available commands: help, whoami, clear",
    whoami: "skyler-cli v0.0.1",
  }

  return (
    <TerminalContextProvider>
      <ReactTerminal
        commands={commands}
        themes={{
          "my-custom-theme": {
            themeBGColor: "#272B36",
            themeToolbarColor: "#DBDBDB",
            themeColor: "#FFFEFC",
            themePromptColor: "#a917a8"
          }
        }}
        theme="my-custom-theme"
      />
    </TerminalContextProvider>
  )
}

export default App
