# root-sdk

<!-- the image cannot be within pypi, so we get it from the sdk website -->
<h1 align="center">
  <img style="vertical-align:middle" height="200" src="https://sdk.rootsignals.ai/en/latest/_images/root_signals+bounding_box.svg">
</h1>

  <!-- This is commented so it is easier to sync with the docs/index.rst -->

  <p align="center">
    <i>Robust AI Skill Management</i>
  </p>

  <p align="center">
      <a href="https://github.com/root-signals/root-python-sdk/releases">
          <img alt="GitHub release"   src="https://img.shields.io/github/release/root-signals/root-python-sdk.svg">
      </a>
      <a href="https://www.python.org/">
              <img alt="Build"   src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg?color=purple">
      </a>
      <a   href="https://github.com/root-signals/root-python-sdk/blob/master/LICENSE">
          <img alt="License"   src="https://img.shields.io/github/license/rootsignals/roots.svg?color=green">
      </a>
  </p>

> Note: We're working with few select organisations, leveraging what we
> learned building root signals, to improve the reliability of their LLM
> systems in production. Due to our small team size, we can only work with
> a few clients, so do write to us at
> [info@rootsignals.com](mailto:info@rootsignals.com), and we will get back
> to you 🙂 Feel free to also open an issue if you find a bug, or create a
> pull request if you come up with a fix or something new.

This SDK provides a way to use Root Signals cloud service, which helps you
evaluate your LLM pipelines. There are existing tools and frameworks that
help you build these pipelines but evaluating it and quantifying your
pipeline performance can be hard. This is where this comes in.

Root Signals provides you with the tools based on the latest research for
evaluating LLM-generated text to give you insights about your LLM
pipeline. It can be integrated with your CI/CD to provide continuous checks
to ensure performance stays within acceptable limits.

## Install

### From pypi

The preferrable way of installing the SDK is from [PyPI](https://pypi.org),
using pip or other package installation of tool of choice. If using pip,
this should be enough:

```bash
pip install root-signals
```

## Quickstart

Please set your API key to environment variable `ROOTSIGNALS_API_KEY`, or to local .env file.

Retrieve an API key from https://app.rootsignals.ai/settings/api-keys

For example:

```bash
export ROOTSIGNALS_API_KEY=somethingreallysecretyougotfromtheweb
```

or, if you prefer using .env file:

```bash
echo ROOTSIGNALS_API_KEY=somethingreallysecretyougotfromtheweb >> .env
```

### Minimal skill
{::comment}examples/minimal.py{:/comment}
```python
from root import RootSignals

# Connect to the Root Signals API
client = RootSignals()

# Create a skill
skill = client.skills.create(
    "Find me good recipes for {{food_type}} food that are {{cuisine}}."
)

# Run it
response = skill.run({"food_type": "spicy", "cuisine": "Korean"})

print(response)

# llm_output="1. Kimchi Jjigae (Kimchi Stew): This spicy and flavorful
# stew is made with fermented kimchi, pork, tofu, and vegetables. ..."
# validation={'validator_results': [], 'is_valid': True}
# model='gpt-3.5-turbo' engine='gpt-3.5-turbo'
# execution_log_id='181eb95b-b972-4e96-8e30-ca7d3447d4fe'
# rendered_prompt='Find me good recipes for spicy food that are
# Korean.'

```

# Documentation

For more details, please see [the main SDK documentation](https://sdk.docs.rootsignals.ai).

# Miscellaneous notes

## Versioning policy

We follow [semantic versioning](https://semver.org); to
point, major versions are not guaranteed to be backwards compatible, minor
versions are, and patch versions only fix bugs.
