/** @type {import('next').NextConfig} */

import path from "path";
import dotenv from "dotenv";
import dotenvExpand from "dotenv-expand";

const loadEnv = (filePath) => {
  const env = dotenv.config({ path: filePath });
  dotenvExpand.expand(env);
};

loadEnv(path.resolve(process.cwd(), ".env.local"));

const apiUrl = process.env.API_URL;

const nextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "utfs.io",
        pathname: `/a/${process.env.NEXT_PUBLIC_UPLOADTHING_APP_ID}/*`,
      },
      {
        protocol: "https",
        hostname: apiUrl,
        pathname: `/api/*`,
      },
    ],
  },
  rewrites: async () => {
    return [
      {
        source: "/api/:path*",
        destination: `${apiUrl}/api/:path*`,
      },
      {
        source: "/docs",
        destination: `${apiUrl}/docs`,
      },
      {
        source: "/openapi.json",
        destination: `${apiUrl}/openapi.json`,
      },
    ];
  },
};

export default nextConfig;
