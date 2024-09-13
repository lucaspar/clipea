# Clipea 📎🟢

> Forked from Dave Hulbert's repository (`dave1010/clipea`). Check out their project for zsh integration and for a better out-of-the-box experience. This is a work in progress with Bash integration and a few opinionated (breaking) changes. Use it at your own risk.

Clipea is a streamlined, cheap and hackable tool that integrates GPT with your console.

> [!CAUTION]
> Be careful with the commands Clipea suggests. Always read and understand them before running.

## Setup

1. Install `uv` and `llm`:

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    uv tool install llm
    llm --version
    # e.g. llm, version 0.16
    ```

2. Configure `llm` to use the model of your choice:

    ```bash
    llm models default gpt-4o
    llm keys set openai
    # paste your openai key from https://platform.openai.com/api-keys
    ```

3. Add the following to your `.bashrc` or `.bash_profile`:

    ```bash
    CLIPEA_HOME= # where you cloned this repo
    alias ??='source ${CLIPEA_HOME}/clipea/bash_wrapper.sh; clipea_wrapper'
    ```

## Usage

### Environment

Clipea gets given some environment limited information like your OS, shell and path.
This allows it to give better responses.

```bash
?? wheres my shell config
?? install curl
?? compare README.md to my clipboard
```

Clipea doesn't have any context of what it said before, though this may be added in the future if there's use cases it helps with.

### More examples

```bash
?? open my shell login script in my editor
?? extract package.tar.gz
?? convert this file.pdf to text, install the tool if needed
?? write a command that generates a 30 char password
```

```bash
?? find files bigger than 10mb
?? rename all txt files space to underscore
?? convert file.avi to gif
?? decrypt data.txt.gpg
```

```bash
?? highlight URLs in index.html
?? show me just the headings from README.md
?? count loc recursively
?? Find replace all PHP files in project that call eval function with safe_eval
?? git fetch, rebase master, safely force push
?? turn orders.csv into a sqlite table
?? count payments in orders.db
```

```bash
?? open bbc news
?? check the spf record for example.com
?? what port is my webserver listening on
?? check cors headers for api.example.com
?? where is nginx writing logs
?? quick http server
```

## Privacy

Clipea uses OpenAI's APIs by default, though can be set to use any LLM that `llm` supports.

Only very basic environment info like your OS and editor is sent to the LLM.
Run `clipea env` or `?? env` to see the data the LLM gets.

## Cost

As a very rough example, using the default GPT-3.5, 100 Clipea queries to OpenAI cost $0.02.
Set a quota and keep an eye on costs to make sure.

## Contributors

See Dave's repo for the original contributors.

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dave1010"><img src="https://avatars.githubusercontent.com/u/50682?v=4?s=100" width="100px;" alt="Dave Hulbert"/><br /><sub><b>Dave Hulbert</b></sub></a><br /><a href="#code-dave1010" title="Code">💻</a> <a href="#ideas-dave1010" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-dave1010" title="Maintenance">🚧</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/edouard-sn"><img src="https://avatars.githubusercontent.com/u/58398928?v=4?s=100" width="100px;" alt="Edouard SENGEISSEN"/><br /><sub><b>Edouard SENGEISSEN</b></sub></a><br /><a href="#code-edouard-sn" title="Code">💻</a> <a href="#ideas-edouard-sn" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-edouard-sn" title="Maintenance">🚧</a> <a href="#platform-edouard-sn" title="Packaging/porting to new platform">📦</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/b-boehne"><img src="https://avatars.githubusercontent.com/u/53817118?v=4?s=100" width="100px;" alt="b-boehne"/><br /><sub><b>b-boehne</b></sub></a><br /><a href="#code-b-boehne" title="Code">💻</a> <a href="#ideas-b-boehne" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/antwxne"><img src="https://avatars.githubusercontent.com/u/59999873?v=4?s=100" width="100px;" alt="Antoine D."/><br /><sub><b>Antoine D.</b></sub></a><br /><a href="#review-antwxne" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lucaspar"><img src="https://avatars.githubusercontent.com/u/7535699?v=4?s=100" width="100px;" alt="Lucas Parzianello"/><br /><sub><b>Lucas Parzianello</b></sub></a><br /><a href="#doc-lucaspar" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://darkstarsystems.com"><img src="https://avatars.githubusercontent.com/u/139975?v=4?s=100" width="100px;" alt="Gary Oberbrunner"/><br /><sub><b>Gary Oberbrunner</b></sub></a><br /><a href="#code-garyo" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/vividfog"><img src="https://avatars.githubusercontent.com/u/75913791?v=4?s=100" width="100px;" alt="vividfog"/><br /><sub><b>vividfog</b></sub></a><br /><a href="#userTesting-vividfog" title="User Testing">📓</a> <a href="#ideas-vividfog" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
