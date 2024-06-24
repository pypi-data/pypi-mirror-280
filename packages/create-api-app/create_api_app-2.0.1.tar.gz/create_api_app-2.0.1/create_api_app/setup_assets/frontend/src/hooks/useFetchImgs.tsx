import { UTListFileUrl } from "@/lib/constants";
import { zip } from "@/lib/utils";
import { UTImage } from "@/types/api";
import { useEffect, useState } from "react";

const useFetchImgs = (imgNames: string) => {
  const [imgUrls, setImgUrls] = useState<UTImage[]>([]);
  const [isLoading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!imgNames) {
      return;
    }

    const fetchUrl = async () => {
      try {
        const response = await fetch(`${UTListFileUrl}?filenames=${imgNames}`, {
          headers: {
            Accept: "application/json",
            method: "GET",
          },
        });

        if (response.ok) {
          const urlTemplate = `https://utfs.io/a/${process.env.NEXT_PUBLIC_UPLOADTHING_APP_ID}`;
          let imgUrls: UTImage[] = [];

          const data: string[] = await response.json();
          const imgData = zip(imgNames.split(","), data);

          imgData.map(([name, url]) => {
            imgUrls.push({
              name: name,
              url: `${urlTemplate}/${url}`,
            });
          });

          setImgUrls(imgUrls);
        }
      } catch (error: any) {
        console.error("Error fetching images:", error);
        setError(error);
      } finally {
        setLoading(false);
      }
    };

    fetchUrl();
  }, [imgNames]);

  return { imgUrls, isLoading, error };
};

export default useFetchImgs;
