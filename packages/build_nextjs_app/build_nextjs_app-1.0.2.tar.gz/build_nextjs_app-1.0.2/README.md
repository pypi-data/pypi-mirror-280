# Build NextJS App

A simple tool for creating fresh [Next.js](https://nextjs.org/) applications using a Docker container with [Bun](https://bun.sh/). The image is updated every two weeks to maintain the latest package versions.

Found on:

- [PyPi](https://pypi.org/project/build_nextjs_app/)
- [Docker Hub](https://hub.docker.com/r/achronus/nextjs_app)
- [GitHub](https://github.com/Achronus/build-nextjs-app/)

It consists of the following packages, libraries and frameworks:

- [Shadcn/ui](https://ui.shadcn.com/)
- [Uploadthing](https://uploadthing.com/)
- [dotenv](https://www.npmjs.com/package/dotenv)
- [dotenv-expand](https://www.npmjs.com/package/dotenv-expand)
- [Lucide React Icons](https://lucide.dev/)
- [Clerk](https://clerk.com/)
- [Stripe](https://docs.stripe.com/stripe-js/react?locale=en-GB)
- [Tailwind CSS](https://tailwindcss.com/)

## Why This Tool?

Looking to spend less time messing with configuration settings? Eager to jump straight into coding! Well you've come to the right place!

This tool builds a set of frontend files quickly with a single command, while maintaining the following key aspects:

1. Compatibility across devices
2. File isolation with easy copying
3. Maximising package build speed using [bun](https://bun.sh/) without issues on `Windows` (`npm` is slow!)
4. Automatic package updates to their latest version often

To achieve this, we use Docker with GitHub actions.

## How To Use It

1. Firstly, [install Docker](https://docs.docker.com/get-docker/)

2. Next, install the package through pip using:

   ```python
   pip install build_nextjs_app
   ```

3. Run it with your desired `project_name`

   ```python
   build-nextjs-app <project_name>
   ```

And that's it! Open the project folder and you'll see a directory called `frontend` with all the assets.

## Need a Backend Too?

We personally use this in our [create-api-app](https://github.com/Achronus/create-api-app) tool for building applications with a FastAPI backend and NextJS frontend.

If you are looking for a FastAPI backend as well, consider trying the tool out!
