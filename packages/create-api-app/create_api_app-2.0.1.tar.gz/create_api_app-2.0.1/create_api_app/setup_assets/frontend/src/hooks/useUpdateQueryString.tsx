import { useSearchParams } from "next/navigation";
import { useCallback } from "react";

/**
 * Create a new `searchParams` string by merging the current `searchParams` with a set of new key-value pairs
 * @param queries an array of name, value pairs for the queries to update
 * @param remove an array of query names to remove from the query string
 * @returns an updated `searchParams` query string starting with a `?`
 */
const useUpdateQueryString = () => {
  const searchParams = useSearchParams();

  const updateQueryString = useCallback(
    (queries: { name: string; value: string }[], remove?: string[]) => {
      const params = new URLSearchParams(searchParams?.toString());

      queries.forEach(({ name, value }) => {
        params.set(name, value);
      });

      if (remove) {
        remove.forEach((query) => {
          params.delete(query);
        });
      }

      return `?${params.toString()}`;
    },
    [searchParams]
  );

  return updateQueryString;
};

export default useUpdateQueryString;
