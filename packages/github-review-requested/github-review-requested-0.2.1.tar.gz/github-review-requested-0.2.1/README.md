# Github review requested

## About the project
To find reviews that are assigned to me and not the whole team, I find it very hard on GitHub. There is https://github.com/pulls/review-requested, but it's not sorted as I want, and I cannot filter with issues that explicitly mention me as a reviewer.

I created this tool to have a clear view of what I need to review. It shows in bold if I am explicitly on the list of reviewers and which person on my team is also on the list.

## Getting started

### Installation

1. Add a token to your GitHub account (don't forget to copy it somewhere): https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic
2. Install python >= 3.8 and pip if you don't have them yet.
3. Install via pip
```sh
pip install github-review-requested
```

<!-- USAGE EXAMPLES -->
## Usage
```bash
Usage: github-review-requested [OPTIONS]

Options:
--user TEXT User name from github [required]
--org TEXT Org name from github [required]
--token TEXT Token from github [required]
--team TEXT Team name from github [required]
--help Show this message and exit.

❯ github-review-requested --user <user_name> --org <org> --team <team_name> --token <token>
```

You need a token from GitHub. Follow this documentation: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic

<!-- ROADMAP -->
## Roadmap
- [x] Have an initial tool that works
- [x] Make PR names clickable to open the PR in the browser
- [x] Option to filter out draft PRs
- [x] Add a loading spinner
- [x] Option to sort by update ascending or descending
- [ ] Store the token in a secure way (also user, org and team?)
- [ ] Add tests
- [ ] Add a screenshot in this readme file
- [ ] More colors! If PRs are too old, show them in red
- [ ] Show already commented requests
- [ ] Filter out issues where tests are not passing

<!-- LICENSE -->
## License

Distributed under the MIT License.

<!-- CONTACT -->
## Contact
Project Link: [https://github.com/mathieumontgomery/github-review-requested](https://github.com/mathieumontgomery/github-review-requested)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->