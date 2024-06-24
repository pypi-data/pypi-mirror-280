# Create API App Quickstart Tool

Welcome to the quickstart tool for creating a `FastAPI` project with a `NextJS` frontend.

This tool is intended to be dynamic and installs the most recent packages where possible, while maintaining compatibility across the main OS's (Mac, Linux and Windows). You can use the tool by installing the `PIP` package. See the [Using The Tool section](#using-the-tool) for more details.

If there are any issues using the tool, please flag them in the [issues](https://github.com/Achronus/create-api-app/issues) section of this repository.

Found on:

- [PyPi](https://pypi.org/project/create-api-app/)
- [GitHub](https://github.com/Achronus/create-api-app/)

## Why This Tool?

Creating a project from scratch can be a tedious process. Not only do you have to create all the files yourself, it typically requires a lot of small minor changes that can easily be automated. So, rather than wasting a lot of time setting up projects, I created a tool that does it all for me!

I use this tool personally for `SaaS` and `ML API` projects and have found it extremely useful for immediately diving into coding without faffing around with setup details (except for configuring API keys). Hopefully, it's useful to you too!

## The Stack

All projects are created using the same stack, consisting of the following:

1. Backend

   - [FastAPI](https://github.com/tiangolo/fastapi)
   - [MongoDB](https://www.mongodb.com/)
   - [Beanie](https://beanie-odm.dev/)
   - [Poetry](https://python-poetry.org/)
   - [Pytest](https://docs.pytest.org/)
   - [Hypothesis](https://hypothesis.readthedocs.io/)

2. Frontend

   - [NextJS](https://nextjs.org/)
   - [TailwindCSS](https://tailwindcss.com/)
   - [Uploadthing](https://uploadthing.com/)
   - [Clerk](https://clerk.com/docs/quickstarts/nextjs)
   - [Stripe](https://stripe.com/docs)
   - [Lucide React](https://lucide.dev/)
   - [Shadcn UI](https://ui.shadcn.com/)

_Note: all libraries and packages are automatically installed to their latest versions when running the tool._

### Useful Styling Options

- [Clerk Themes](https://clerk.com/docs/components/customization/themes)
- [Shadcn UI Theme Generator](https://gradient.page/tools/shadcn-ui-theme-generator)
- [Modern Background Snippets](https://bg.ibelick.com/)

## Using The Tool

1. Firstly, install [Docker](https://docs.docker.com/get-docker/), we use this to create the frontend files dynamically using the [Build NextJS App Tool](https://github.com/Achronus/build-nextjs-app).

2. Install the package through `PIP` using the following command (requires `Python 3.12` minimum):

   ```python
   pip install create_api_app
   ```

3. Create a project with the following command:

   ```python
   create-api-app <project_name>
   ```

And that's it! You'll find two folders in your project, one called `frontend` (for NextJS) and another called `backend` (for FastAPI).
