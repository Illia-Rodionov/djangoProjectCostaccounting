SELECT COUNT(notebooks_brand.title), notebooks_brand.title
FROM notebooks_brand
    LEFT JOIN notebooks_notebook
        ON notebooks_brand.id = notebooks_notebook.brand_id GROUP BY notebooks_brand.title
                                                            ORDER BY COUNT(notebooks_brand.title) DESC
