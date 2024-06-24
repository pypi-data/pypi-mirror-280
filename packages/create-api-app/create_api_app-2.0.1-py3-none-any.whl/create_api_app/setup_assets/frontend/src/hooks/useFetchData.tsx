import { useEffect, useState } from "react";

const useFetchData = <T,>(url: string) => {
  const [data, setData] = useState<T | null>(null);
  const [isLoading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!url) {
      return;
    }

    const fetchData = async () => {
      try {
        const response = await fetch(url);

        if (response.ok) {
          const result = await response.json();
          setData(result);
        }
      } catch (error: any) {
        console.error("Error fetching data:", error);
        setError(error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [url]);

  return { data, isLoading, error };
};

export default useFetchData;
